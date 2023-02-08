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

namespace MP05_BieuDoHistogramAnhMauRGB
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
            //Load original image in Imagebox
            IBor.Image = imgor;
            /*--------------------------------------------*/
            //Calculate Histogram
            double[,] histogram = HistogramCalculation(imgor);
            //Convert datatype
            List<PointPairList> points = HistogramConvert(histogram);
            //Draw histogram diagram and show it
            zHistogramRGB.GraphPane = HistogramDiagram(points);
            zHistogramRGB.Refresh();
        }

        //Calculate Histogram of Grayscale picture
        public double[,] HistogramCalculation(Image<Bgr, byte> bmp)
        {
            //We use 2-diemnsion matrix to contain the histogram's infomations for each channel: R,G,B
            double[,] histogram = new double[3, 256]; // 3 is the num of channel need saving, 256 is the amount need to contain color value from 0 to 255
            for (int x = 0; x < bmp.Width; x++)
                for (int y = 0; y < bmp.Height; y++)
                {
                    //Get pixels value from graypic
                    Bgr pixel = bmp[y, x];
                    byte r = (byte)pixel.Red;
                    byte g = (byte)pixel.Green;
                    byte b = (byte)pixel.Blue;
                    histogram[0, r]++; //Histogram of channel r
                    histogram[1, g]++; //Histogram of channel g
                    histogram[2, b]++; //Histogram of channel b
                }
            return histogram; //Return 2-dimension matrix concluding infomations of RGB
        }
        List<PointPairList> HistogramConvert(double[,] histogram)
        {
            //Use a matrix doesn't need to declare the amount of components to contain changing value
            List<PointPairList> points = new List<PointPairList>();
            PointPairList redPoints = new PointPairList(); //Convert histogram channel R
            PointPairList greenPoints = new PointPairList(); //Convert histogram channel G
            PointPairList bluePoints = new PointPairList(); //Convert histogram channel B
            for (int i = 0; i < 256; i++)
            {
                //i í the horizontal axis, from 0 - 255
                //histogram[i] is the vertical axis, which is the value of the grayscale value 
                redPoints.Add(i, histogram[0, i]);//Convert for channel R
                greenPoints.Add(i, histogram[1, i]);//Convert for channel R
                bluePoints.Add(i, histogram[2, i]);//Convert for channel R
            }
            points.Add(redPoints);
            points.Add(greenPoints);
            points.Add(bluePoints);
            return points;
        }
        //Establish a Diagram in Zedgraph
        public GraphPane HistogramDiagram(List<PointPairList> histogram)
        {
            //GraphPane is a diagram component in Zedgraph
            GraphPane gp = new GraphPane();
            gp.Title.Text = @"Histogram Diagram"; //The tittle
            gp.Rect = new Rectangle(0, 0, 500, 500); //Fram consists diagram
            //Establish the horizontal axis
            gp.XAxis.Title.Text = @"The pixel value of RGB image";
            gp.XAxis.Scale.Min = 0; //minimum = 0
            gp.XAxis.Scale.Max = 255; //maximum = 255
            gp.XAxis.Scale.MajorStep = 5; //Each time increase by 5 main unit
            gp.XAxis.Scale.MinorStep = 1; //Each time increase by 1 unit in each main unit = 1
            //Establish the vertical axis
            gp.YAxis.Title.Text = @"The amount of RGB pixels have the same value";
            gp.YAxis.Scale.Min = 0; //minimum = 0
            gp.YAxis.Scale.Max = 15000; //This figure must bigger than the dimension of picture (w x h)
            gp.YAxis.Scale.MajorStep = 5; //Each time increase by 5 main unit
            gp.YAxis.Scale.MinorStep = 1; //Each time increase by 1 unit in each main unit = 1
            //Use bar diagram to present Histogram
            gp.AddBar("Histogram's Red", histogram[0], Color.Red);
            gp.AddBar("Histogram's Green", histogram[1], Color.Green);
            gp.AddBar("Histogram's Blue", histogram[2], Color.Blue);
            return gp;
        }

        private void zHistogramRGB_Load(object sender, EventArgs e)
        {

        }
    }
}
