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

namespace MP04_ChuyenAnhMauRGBSangAnhNhiPhan
{
    public partial class Form1 : Form
    {
        Image<Bgr, byte> imgor;
        public Form1()
        {
            InitializeComponent();
            //Image path
            string img = @"C:\Users\DELL\Desktop\lena_color.jpg";
            //Read Image
            imgor = new Image<Bgr, byte>(img);
            //Load original image in Imagebox
            IBor.Image = imgor;
            //Load Lightness Grayscale Image in Imagebox
            IBlgt.Image = RGBLightnessConvert(imgor);
            //Load Average Grayscale Image in Imagebox
            IBavg.Image = RGBAverageConvert(imgor);
            //Load Luminace Grayscale Image in Imagebox
            IBlum.Image = RGBLuminaceConvert(imgor);
            //Load Binary Image in Imagebox
            //IBbn.Image = RGBBinaryConvert(imgor, 100); (don't need this line of code)

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
                    byte gray = (byte)((max + min) / 2);
                    //Set red image pixel
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
                    byte gray = (byte)(0.0722 * b + 0.7152 * g + 0.2126 * r);
                    //Set red image pixel
                    graypic[y, x] = new Bgr(gray, gray, gray);
                }
            }
            return graypic;
        }
        public Image<Bgr, byte> RGBBinaryConvert(Image<Bgr, byte> imgor, byte threshold)
        {
            int width = imgor.Width;
            int height = imgor.Height;
            Image<Bgr, byte> binarypic = new Image<Bgr, byte>(width, height);
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
                    byte binary = (byte)(0.0722 * b + 0.7152 * g + 0.2126 * r);
                    //Classify pixel to binary value based on threshold value
                    if (binary < threshold)
                        binary = 0;
                    else
                        binary = 255;
                    //Set calculated binary pixel to binarypic
                    binarypic[y, x] = new Bgr(binary, binary, binary);
                }
            }
            return binarypic;
        }
        private void label2_Click(object sender, EventArgs e)
        {
        }
        private void label5_Click(object sender, EventArgs e)
        {

        }
        private void BinaScrollbar_ValueChanged(object sender, EventArgs e)
        {
            //Take the threshold value from scrollbar
            //The return value of scrollbar is int type, so we need to set it in byte
            byte threshold = (byte)BinaScrollbar.Value;
            
            //Show threshold value
            IBThreshold2.Text = threshold.ToString();
            //Call the binary function
            IBbn.Image = RGBBinaryConvert(imgor, threshold);
        }
    }
}
