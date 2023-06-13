#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
using namespace std;
int Distance[100][100], cost = 0, CityNum, completed[100];//申明一个二维数组存放城市间的距离

void Readcoordinatetxt(string txtfilename)//读取城市坐标文件的函数
{
    int coordinate[2][100];
    int Citycount = 100;
    ifstream myfile;
    myfile.open(txtfilename);
    int x, y, z;
    int i = 0;
    while (!myfile.eof() && (myfile >> z >> x >> y))
    {
        coordinate[0][i] = x;
        coordinate[1][i] = y;
        i++;
    }
    myfile.close();

    //计算城市距离矩阵
    int pi = 0, ki = 0;
    for (; pi < 100; pi++)
        for (; ki < 100; ki++)
        {
            Distance[pi][ki] = sqrt((pow((coordinate[0][pi] - coordinate[0][ki]), 2) + pow((coordinate[1][pi] - coordinate[1][ki]), 2)) / 10.0);//计算城市pi,ki之间的伪欧式距离
            if (round(Distance[pi][ki] < Distance[pi][ki]))Distance[pi][ki] = round(Distance[pi][ki]) + 1;
            else Distance[pi][ki] = round(Distance[pi][ki]);
        }
}


void takeInput() 
{
    int i, j;

    cout << "Enter the number of cities: "<<endl;
    cin >> CityNum;
    cout << "Enter the Cost Matrix"<<endl;

    for (i = 0; i < CityNum; i++) {
        cout << "Enter Elements of Row: " << i + 1 << endl;

        for (j = 0; j < CityNum; j++)
            cin >> Distance[i][j];

        completed[i] = 0;
    }

    cout << "The cost list is:"<<endl;

    for (i = 0; i < CityNum; i++) {
        for (j = 0; j < CityNum; j++)
            cout << "\t" << Distance[i][j];
        cout << endl;
    }
}

int least(int c) {
    int i, nc = 999;
    int min = 999, kmin;
    
    for (i = 0; i <CityNum; i++) {
        if ((Distance[c][i] != 0) && (completed[i] == 0))//有路径存在，且点没有被访问过
            if (Distance[c][i] < min) {
                min = Distance[c][i];
                nc = i;
            }
    }
    if (min != 999)
        cost += min;
    return nc;
}

void mincost(int city) {
    int i, NextCity;
    completed[city] = 1;
    cout << city + 1 << " to ";
    NextCity = least(city);
    
    if (NextCity == 999) {
        NextCity = 0;
        cout << NextCity + 1<<endl;
        cost += Distance[city][NextCity];
        return ;
    }
    mincost(NextCity);//递归
}

int main() {
    //takeInput();
    Readcoordinatetxt("CityData.txt");
    cout << "The Path is:"<<endl;
    mincost(0); // passing 0 because starting vertex
    cout << "Minimum cost is " << cost<<endl;

    return 0;
}