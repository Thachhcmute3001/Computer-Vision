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
using ZedGraph;

namespace BieuDoHistogram
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            //Image path
            string img = @"C:\Users\DELL\Desktop\lena.jpg";
            //Read Image
            Image<Bgr, byte> imgor = new Image<Bgr, byte>(img);
            Image<Bgr, byte> graypic = RGBLuminaceConvert(imgor);
            //Load original image in Imagebox
            IBor.Image = imgor;
            //Load Luminace Grayscale Image in Imagebox
            IBlum.Image = graypic;
            //Call functions to draw Histogram
            /*--------------------------------------------*/
            //Calculate Histogram
            double[] histogram = HistogramCalculation(graypic);
            //Convert datatype
            PointPairList points = HistogramConvert(histogram);
            //Draw histogram diagram and show it
            zHistogram.GraphPane = HistogramDiagram(points);

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
        //Calculate Histogram of Grayscale picture
        public double[] HistogramCalculation(Image<Bgr, byte> graypic)
        {
            //Each grayscale pixel has value 
            double[] histogram = new double[256];
            for (int x = 0; x < graypic.Width; x++)
                for (int y = 0; y < graypic.Height; y++)
                {
                    //Get pixels value from graypic
                    Bgr pixel = graypic[y, x];
                    //Extract ARGB value from pixel
                    byte gray = (byte)pixel.Red; //In grayscale picture, the value of channel R equals to B and G
                    //The calculated value of gray is the corresponding parameter of histogram matrix, then increase the value of histogram matrix 1 digit
                    histogram[gray]++;
                }
            return histogram;
        }
        PointPairList HistogramConvert(double[] histogram)
        {
            //PointPair list is a datatypes of Zedgraph to draw graph
            PointPairList points = new PointPairList();
            for (int i = 0; i < histogram.Length; i++)
            {
                //i í the horizontal axis, from 0 - 255
                //histogram[i] is the vertical axis, which is the value of the grayscale value 
                points.Add(i, histogram[i]);
            }
            return points;
        }
        //Establish a Diagram in Zedgraph
        public GraphPane HistogramDiagram(PointPairList histogram)
        {
            //GraphPane is a diagram component in Zedgraph
            GraphPane gp = new GraphPane();
            gp.Title.Text = @"Histogram Diagram"; //The tittle
            gp.Rect = new Rectangle(0, 0, 500, 500); //Fram consists diagram
            //Establish the horizontal axis
            gp.XAxis.Title.Text = @"The pixel value of grayscale image";
            gp.XAxis.Scale.Min= 0; //minimum = 0
            gp.XAxis.Scale.Max= 255; //maximum = 255
            gp.XAxis.Scale.MajorStep = 5; //Each time increase by 5 main unit
            gp.XAxis.Scale.MinorStep = 1; //Each time increase by 1 unit in each main unit = 1
            //Establish the vertical axis
            gp.YAxis.Title.Text = @"The amount of grayscale pixels have the same value";
            gp.YAxis.Scale.Min = 0; //minimum = 0
            gp.YAxis.Scale.Max = 15000; //This figure must bigger than the dimension of picture (w x h)
            gp.YAxis.Scale.MajorStep = 5; //Each time increase by 5 main unit
            gp.YAxis.Scale.MinorStep = 1; //Each time increase by 1 unit in each main unit = 1
            //Use bar diagram to present Histogram
            gp.AddBar("Histogram", histogram, Color.LightGreen);
            return gp;
        }

        private void Histogram_Load(object sender, EventArgs e)
        {
            
        }
    }
}
