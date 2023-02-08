using Emgu.CV.Structure;
using Emgu.CV;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.CV.Util;

namespace MP03_ChuyenAnhMauRGBSangAnhMauMucXam
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
            //Load original image in Imagebox
            IBor.Image = imgor;
            //Load Lightness Grayscale Image in Imagebox
            IBlgt.Image = RGBLightnessConvert(imgor);
            //Load Average Grayscale Image in Imagebox
            IBavg.Image = RGBAverageConvert(imgor);
            //Load Luminace Grayscale Image in Imagebox
            IBlum.Image = RGBLuminaceConvert(imgor);

        }
        public Image<Bgr, byte> RGBLightnessConvert(Image<Bgr, byte> imgor)
        {
            int width = imgor.Width;
            int height = imgor.Height;
            Image<Bgr, byte> graypic = new Image<Bgr, byte>(width, height);
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //Get pixel value
                    Bgr pixel = imgor[y, x];
                    //Extract ARGB value from pixel
                    byte b = (byte)pixel.Blue;
                    byte g = (byte)pixel.Green;
                    byte r = (byte)pixel.Red;

                    //Calculate the grayscale for each pixels
                    byte max = Math.Max(r, Math.Max(g, b));
                    byte min = Math.Min(r, Math.Max(g, b));
                    byte gray = (byte) ((max + min) / 2);
                    //Set image pixel
                    graypic[y, x] = new Bgr(gray, gray, gray);

                }
            }
            return graypic;
        }
        public Image<Bgr, byte> RGBAverageConvert(Image<Bgr, byte> imgor)
        {
            int width = imgor.Width;
            int height = imgor.Height;
            Image<Bgr, byte> graypic = new Image<Bgr, byte>(width, height);
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //Get pixel value
                    Bgr pixel = imgor[y, x];
                    //Extract ARGB value from pixel
                    byte b = (byte)pixel.Blue;
                    byte g = (byte)pixel.Green;
                    byte r = (byte)pixel.Red;

                    //Calculate the grayscale for each pixels
                    byte gray = (byte)((b + g + r) / 3);
                    //Set red image pixel
                    graypic[y, x] = new Bgr(gray, gray, gray);

                }
            }
            return graypic;
        }
        public Image<Bgr, byte> RGBLuminaceConvert(Image<Bgr, byte> imgor)
        {
            int width = imgor.Width;
            int height = imgor.Height;
            Image<Bgr, byte> graypic = new Image<Bgr, byte>(width, height);
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //Get pixel value
                    Bgr pixel = imgor[y, x];
                    //Extract ARGB value from pixel
                    byte b = (byte)pixel.Blue;
                    byte g = (byte)pixel.Green;
                    byte r = (byte)pixel.Red;

                    //Calculate the grayscale for each pixels
                    byte gray = (byte)(0.0722*b + 0.7152*g + 0.2126*r);
                    //Set red image pixel
                    graypic[y, x] = new Bgr(gray, gray, gray);

                }
            }
            return graypic;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
