#include <pcl/point_cloud.h>
#include <pcl/kdtree/kdtree_flann.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

string gps_u = "/home/sam/Downloads/gps_unorder.txt";
string gps_o = "/home/sam/Downloads/gps_order.txt";
string ekf_u = "/home/sam/Downloads/ekf_unorder.txt";
string ekf_o = "/home/sam/Downloads/ekf_order.txt";
string dist_file = "/home/sam/Downloads/distance.txt";
string err_file = "/home/sam/Downloads/error.txt";

struct mytuple
{
    float x, y;
    mytuple(float x_, float y_):x(x_), y(y_){}
};

int main (int argc, char** argv)
{
    fstream file;
    file.open(gps_o);
    float x, y;
    std::vector<mytuple> gps_vec;
    while (!file.eof())
    {
        file >> x >> y;
        gps_vec.push_back(mytuple(x, y));
    }
    file.close();

    size_t size = gps_vec.size();
    pcl::PointCloud<pcl::PointXYZI>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZI>);
    cloud->points.resize(size);

    for (std::size_t i = 0; i < size; ++i)
    {
        cloud->points[i].x = gps_vec[i].x;
        cloud->points[i].y = gps_vec[i].y;
        cloud->points[i].z = 0;
    }

    pcl::KdTreeFLANN<pcl::PointXYZI> kdtree;
    kdtree.setInputCloud(cloud);

    file.open(ekf_o);
    std::vector<mytuple> ekf_vec;
    while (!file.eof())
    {
        file >> x >> y;
        ekf_vec.push_back(mytuple(x, y));
    }
    file.close();

    pcl::PointXYZI searchPoint;
    int K = 1;
    
    std::vector<float> dist;
    std::vector<float> err;
    size_t n = 0;
    float td = 0.0;

    for (size_t i = 0; i < ekf_vec.size(); i++)
    {
        // cout<<"n: "<<n<<endl;
        if (i%100 == 0)
        {
            td += sqrt(pow(ekf_vec[i].x - ekf_vec[n].x, 2) + pow(ekf_vec[i].y - ekf_vec[n].y, 2));
            n = i;
            
        }
            
        searchPoint.x = ekf_vec[i].x;
        searchPoint.y = ekf_vec[i].y;
        searchPoint.z = 0;
        std::vector<int> pointIdxNKNSearch(K);
        std::vector<float> pointNKNSquaredDistance(K);
        if (kdtree.nearestKSearch(searchPoint, K, pointIdxNKNSearch, pointNKNSquaredDistance) > 0)
        {
            float x = cloud->points[pointIdxNKNSearch[0]].x;
            float y = cloud->points[pointIdxNKNSearch[0]].y;
            float d = pow(x - searchPoint.x, 2) + pow(y - searchPoint.y, 2);
            dist.push_back(sqrt(d));
            if (i%100 == 0)
            {
                if (td > 0)
                {
                    err.push_back(d/td);
                    // cout<<i<<": "<<d/td<<endl;
                }
                else
                {
                    err.push_back(0.0);
                    // cout<<i<<": "<<0<<endl;
                }
            }
            
            // for (std::size_t i = 0; i < pointIdxNKNSearch.size (); ++i)
            //     std::cout << "    "  <<   cloud->points[ pointIdxNKNSearch[i] ].x 
            //             << " " << cloud->points[ pointIdxNKNSearch[i] ].y 
            //             << " " << cloud->points[ pointIdxNKNSearch[i] ].z 
            //             << " (squared distance: " << pointNKNSquaredDistance[i] << ")" << std::endl;
        }
    }
    std::sort(dist.begin(), dist.end());
    cout<<"total distance: "<<td<<endl;
    cout<<"min: "<<dist[0]<<", max: "<<dist[dist.size()-1]<<endl;
    
    cout<<"writing file: "<<dist_file<<endl;
    ofstream f;
    f.open(dist_file);
    for (std::vector<float>::iterator it = dist.begin(); it != dist.end(); it++)
        f << *it << "\n";
    f.close();

    f.open(err_file);
    for (std::vector<float>::iterator it = err.begin(); it != err.end(); it++)
        f << *it << "\n";
    f.close();

    // Neighbors within radius search
    // std::vector<int> pointIdxRadiusSearch;
    // std::vector<float> pointRadiusSquaredDistance;
    // float radius = 256.0f * rand () / (RAND_MAX + 1.0f);
    // std::cout << "Neighbors within radius search at (" << searchPoint.x 
    //         << " " << searchPoint.y 
    //         << " " << searchPoint.z
    //         << ") with radius=" << radius << std::endl;
    // if ( kdtree.radiusSearch (searchPoint, radius, pointIdxRadiusSearch, pointRadiusSquaredDistance) > 0 )
    // {
    //     for (std::size_t i = 0; i < pointIdxRadiusSearch.size (); ++i)
    //         std::cout << "    "  <<   cloud->points[ pointIdxRadiusSearch[i] ].x 
    //                 << " " << cloud->points[ pointIdxRadiusSearch[i] ].y 
    //                 << " " << cloud->points[ pointIdxRadiusSearch[i] ].z 
    //                 << " (squared distance: " << pointRadiusSquaredDistance[i] << ")" << std::endl;
    // }

    return 0;
}
