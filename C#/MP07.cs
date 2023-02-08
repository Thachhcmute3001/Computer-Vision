using Emgu.CV.Structure;
using Emgu.CV;
using Emgu.CV.Util;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MP07_RGBToHSI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            //Image path
            string img = @"C:\Users\DELL\Desktop\lena_color.jpg";
            //Read Image
            Image<Bgr, byte> imgor = new Image<Bgr, byte>(img);
            //Show color HSI channel converted from RGB
            List<Image<Bgr, byte>> HSI = HSIToRGBConvert(imgor);
            //Load original image in Imagebox
            IBor.Image = imgor;
            //Load Hue Image in Imagebox
            IBhue.Image = HSI[0];
            //Load Saturation Image in Imagebox
            IBsat.Image = HSI[1];
            //Load Yellow Image in Imagebox
            IBits.Image = HSI[2];
            //Load Black Image in Imagebox
            IBhsi.Image = HSI[3];


        }
        public List<Image<Bgr, byte>> HSIToRGBConvert(Image<Bgr, byte> imgor)
        {
            List<Image<Bgr, byte>> HSI = new List<Image<Bgr, byte>>();
            //Get image dimension
            int width = imgor.Width;
            int height = imgor.Height;
            //3 copy blank image has the same dimension as imgor's to contain 3 parameters of H, S, I channel
            Image<Bgr, byte> Hue = new Image<Bgr, byte>(height, width);
            Image<Bgr, byte> Saturation = new Image<Bgr, byte>(height, width);
            Image<Bgr, byte> Intensity = new Image<Bgr, byte>(height, width);
            //HSI Image (combined by 3 channels H-S-I)
            Image<Bgr, byte> HSIimg = new Image<Bgr, byte>(height, width);
            for (int x = 0; x < width; x++)
            {
                for (int y = 0; y < width; y++)
                {
                    //Get pixel value
                    Bgr pixel = imgor[x, y];
                    //Extract ARGB value from pixel
                    //We need to use "double" datatype for b, g, r because the return value after we calculate
                    //H-S-I parameters will be double
                    double b = pixel.Blue;
                    double g = pixel.Green;
                    double r = pixel.Red;
                    //--------------------------//
                    //H-S-I equations
                    //Numerator
                    double num = ((r - g) + (r - b)) / 2;
                    //Denominator
                    double deno = Math.Sqrt((r - g) * (r - g) + (r - b) * (g - b));
                    //The return value of Acos function in C#.NET is radian
                    double theta = Math.Acos(num / deno);
                    //--------------------------//
                    //The Hue equation
                    double H = 0;
                    if (b <= g) 
                        H = theta;
                    else if (b > g) 
                        H = (2 * Math.PI) - theta;
                    //Convert radian to degree
                    H = H * 180 / Math.PI;
                    //-------------------------//
                    //The Saturation equation
                    //Get min value of R, G, B
                    double min = Math.Min(r, Math.Min(g, b)); 
                    // Main equation
                    double S = 1 - 3 * min / (r + g + b);
                    //Because the value we take from above equation is in range [0,1]
                    //To show it, we need to convert S to the range[0, 255]
                    S = S * 255;
                    //The Intensity equation
                    //is the Average grayscale equation
                    double I = (r + g + b) / 3;
                    //Set image pixel
                    Hue[x, y] = new Bgr((byte)H, (byte)H, (byte)H); //Bgr(double blue, double green, double red)
                    Saturation[x, y] = new Bgr((byte)S, (byte)S, (byte)S);
                    Intensity[x, y] = new Bgr((byte)I, (byte)I, (byte)I);
                    HSIimg[x, y] = new Bgr((byte)I, (byte)S, (byte)H);
                }
                HSI.Add(Hue);
                HSI.Add(Saturation);
                HSI.Add(Intensity);
                HSI.Add(HSIimg);
            }
            return HSI;

        }

    }
}
