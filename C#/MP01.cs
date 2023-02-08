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

namespace MP01_HienThiAnhMauRGB
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            //Image path
            string img = @"C:\Users\DELL\Desktop\lena_color.jpg";
            //Read Image
            Image<Bgr, byte> imgor = new Image<Bgr, byte>(img); //byte is unsigned int 8 bit
             //Load original image in picturebox1
            IBor.Image = imgor;
            //Get image dimension
            int width = imgor.Width;
            int height = imgor.Height;

            //3 copy images for red green blue images
            Image<Bgr, byte> rbmp = new Image<Bgr, byte>(width, height);
            Image<Bgr, byte> gbmp = new Image<Bgr, byte>(width, height);
            Image<Bgr, byte> bbmp = new Image<Bgr, byte>(width, height);
            //Red green blue image
            for (int x = 0; x < height; x++)
            {
                for(int y = 0; y < width; y++)
                {
                    //Get pixel value
                    Bgr pixel = imgor[y, x];
                    //Extract ARGB value from pixel
                    byte b = (byte)pixel.Blue;
                    byte g = (byte)pixel.Green;
                    byte r = (byte)pixel.Red;

                    //Set image pixel
                    rbmp[y, x] = new Bgr(0, 0, r);
                    gbmp[y, x] = new Bgr(0, g, 0);
                    bbmp[y, x] = new Bgr(b, 0, 0);

                }
            }
            //Load red image
            IBred.Image = rbmp;
            //Load green image
            IBgr.Image = gbmp;
            //Load blue image
            IBbl.Image = bbmp;
        }
    }
}
