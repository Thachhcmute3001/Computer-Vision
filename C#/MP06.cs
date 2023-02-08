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

namespace MP06_RGBToCMYK
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            //Image path
            string img = @"C:\Users\DELL\Desktop\lena30.jpg";
            //Read Image
            Image<Bgr, byte> imgor = new Image<Bgr, byte>(img);
            //Show color CMYK channel converted from RGB
            List<Image<Bgr, byte>> CMYK = RGBToCMYKConvert(imgor);
            //Load original image in Imagebox
            IBor.Image = imgor;
            //Load Cyan Image in Imagebox
            IBcy.Image = CMYK[0];
            //Load Magenta Image in Imagebox
            IBmgt.Image = CMYK[1];
            //Load Yellow Image in Imagebox
            IByll.Image = CMYK[2];
            //Load Black Image in Imagebox
            IBblk.Image = CMYK[3];

        }

        public List<Image<Bgr, byte>> RGBToCMYKConvert(Image<Bgr, byte> imgor)
        {
            //Cyan is the mixed color between Green and Blue, so we just need to set Red = 0
            //Magenta is the mixed color between Red and Blue, so we just need to set Green = 0
            //Yellow is the mixed color between Green and Red, so we just need to set Blue = 0
            //Black is the color that we take min(R, G, B)

            //Create a list containing 4 channel C-M-Y-K
            //List is a matrix in C# that doesn't need to declare the dimension of matrix in advanced
            List<Image<Bgr, byte>> CMYK = new List<Image<Bgr, byte>>();
            int width = imgor.Width;
            int height = imgor.Height;
            Image<Bgr, byte> Cyan = new Image<Bgr, byte>(width, height);
            Image<Bgr, byte> Magenta = new Image<Bgr, byte>(width, height);
            Image<Bgr, byte> Yellow = new Image<Bgr, byte>(width, height);
            Image<Bgr, byte> Black = new Image<Bgr, byte>(width, height);
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
                    //Take the minimum of R,G,B
                    byte min = Math.Min(r, Math.Max(g, b));
                    //Set image pixel
                    Cyan[y, x] = new Bgr(b, g, 0); //Bgr(double blue, double green, double red)
                    Magenta[y, x] = new Bgr(b, 0, r);
                    Yellow[y, x] = new Bgr(0, g, r);
                    Black[y, x] = new Bgr(min, min, min);
                }
                CMYK.Add(Cyan); 
                CMYK.Add(Magenta); 
                CMYK.Add(Yellow); 
                CMYK.Add(Black);
            }
            return CMYK;
        }

            private void label4_Click(object sender, EventArgs e)
        {

        }

        private void IBcy_Click(object sender, EventArgs e)
        {

        }
    }
}
