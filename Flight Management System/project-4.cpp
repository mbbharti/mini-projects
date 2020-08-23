#include <bits/stdc++.h>
using namespace std;

class Graph {
private:
    // number of vertices
    int n=9;

    // adjacency matrix
    int d[15][15]=      { { 0, 4, 0, 0, 0, 0, 0, 8, 0 },
                        { 4, 0, 8, 0, 0, 0, 0, 11, 0 },
                        { 0, 8, 0, 7, 0, 4, 0, 0, 2 },
                        { 0, 0, 7, 0, 9, 14, 0, 0, 0 },
                        { 0, 0, 0, 9, 0, 10, 0, 0, 0 },
                        { 0, 0, 4, 14, 10, 0, 2, 0, 0 },
                        { 0, 0, 0, 0, 0, 2, 0, 1, 6 },
                        { 8, 11, 0, 0, 0, 0, 1, 0, 7 },
                        { 0, 0, 2, 0, 0, 0, 6, 7, 0 } };

    int f[15][15]=      { { 0, 30, 0, 0, 0, 0, 0, 80, 0 },
                        { 70, 0, 40, 0, 0, 0, 0, 100, 0 },
                        { 0, 80, 0, 70, 0, 20, 0, 0, 40 },
                        { 0, 0, 60, 0, 90, 120, 0, 0, 0 },
                        { 0, 0, 0, 80, 0, 110, 0, 0, 0 },
                        { 0, 0, 50, 110, 120, 0, 40, 0, 0 },
                        { 0, 0, 0, 0, 0, 20, 0, 30, 60 },
                        { 90, 80, 0, 0, 0, 0, 20, 0, 70 },
                        { 0, 0, 20, 0, 0, 0, 80, 60, 0 } };

public:

    void displayAdjacencyMatrix()
    {
        cout << "\n\n Adjacency Matrix:\n";

        // displaying the 2D array
        cout<<"Distance matrix:\n";
        for (int i = 0; i < n; ++i) {
            cout << "\n";
            for (int j = 0; j < n; ++j) {
                cout << " " << d[i][j];
            }
        }
        cout<<"\n\nfare matrix:\n";
        for (int i = 0; i < n; ++i) {
            cout << "\n";
            for (int j = 0; j < n; ++j) {
                cout << " " << f[i][j];
            }
        }
        cout<<"\n\n";
    }


    void addAirport()
    {
        // increasing the number of vertices
        n++;
        int i;

        // initializing the new elements to 0
        for (i = 0; i < n; ++i) {
            d[i][n - 1] = 0;
            d[n - 1][i] = 0;
            f[i][n - 1] = 0;
            f[n - 1][i] = 0;
        }
        displayAdjacencyMatrix();
    }

    void removeAirport()
    {
        int x;
        cout<<"Which airport do you want to remove\n";
        cin>>x;
        // checking if the vertex is present
        if (x > n)
        {
            cout << "\nVertex not present!";
            return;
        }
        else
        {
            int i;
            // removing the vertex
            while (x < n)
            {
                // shifting the rows to left side
                for (i = 0; i < n; ++i) {
                    d[i][x] = d[i][x + 1];
                    f[i][x] = f[i][x + 1];
                }

                // shifting the columns upwards
                for (i = 0; i < n; ++i) {
                    d[x][i] = d[x + 1][i];
                    f[x][i] = f[x + 1][i];
                }
                x++;
            }
            // decreasing the number of vertices
            n--;
        }
        displayAdjacencyMatrix();
    }


    void addRoute()
    {
        int x,y,dist,fare;
        cout<<"Enter vertex between whose vertex is to be added\n";
        cin>>x>>y;
        cout<<"Enter distance and fare\n";
        cin>>dist>>fare;
        // checks if the vertex exists in the graph
        if ((x >= n) || (y > n)) {
            cout << "Vertex does not exists!";
        }

        // checks if the vertex is connecting to itself
        if (x == y) {
            cout << "Same Vertex!";
        }
        else {
            // connecting the vertices
            d[y][x] = dist;
            d[x][y] = dist;
            f[y][x] = fare;
            f[x][y] = fare;
        }

        displayAdjacencyMatrix();
    }



    int minDistance(int dist[], bool sptSet[])
    {
        // Initialize min value
        int min = INT_MAX, min_index;

        for (int v = 0; v < n; v++)
            if (sptSet[v] == false && dist[v] <= min)
                min = dist[v], min_index = v;

        return min_index;
    }

    void s2d()
    {
        int src,dest;
        cout<<"\nEnter source and destination node\n";
        cin>>src>>dest;
        int dist[n]; // The output array.  dist[i] will hold the shortest
        // distance from src to i

        bool sptSet[n]; // sptSet[i] will be true if vertex i is included in shortest
        // path tree or shortest distance from src to i is finalized

        // Initialize all distances as INFINITE and stpSet[] as false
        for (int i = 0; i < n; i++)
            dist[i] = INT_MAX, sptSet[i] = false;

        // Distance of source vertex from itself is always 0
        dist[src] = 0;

        // Find shortest path for all vertices
        for (int count = 0; count < n - 1; count++) {
            // Pick the minimum distance vertex from the set of vertices not
            // yet processed. u is always equal to src in the first iteration.
            int u = minDistance(dist, sptSet);
            if(u==dest)
            {
                cout<<"\nMinimum distance from "<<src<<" to "<<dest<<" = ";
                cout<<dist[dest]<<"\n\n";
            }
            // Mark the picked vertex as processed
            sptSet[u] = true;

            // Update dist value of the adjacent vertices of the picked vertex.
            for (int v = 0; v < n; v++)

                // Update dist[v] only if is not in sptSet, there is an edge from
                // u to v, and total weight of path from src to  v through u is
                // smaller than current value of dist[v]
                if (!sptSet[v] && d[u][v] && dist[u] != INT_MAX
                    && dist[u] + d[u][v] < dist[v])
                    dist[v] = dist[u] + d[u][v];
        }
    }


    void an2ad()
    {
        int src;
        for(int src=0;src<n;src++)
        {
        cout<<"\nSource node is " <<src<<endl;
        //cin>>src;
        int dist[n]; // The output array.  dist[i] will hold the shortest
        // distance from src to i

        bool sptSet[n]; // sptSet[i] will be true if vertex i is included in shortest
        // path tree or shortest distance from src to i is finalized

        // Initialize all distances as INFINITE and stpSet[] as false
        for (int i = 0; i < n; i++)
            dist[i] = INT_MAX, sptSet[i] = false;

        // Distance of source vertex from itself is always 0
        dist[src] = 0;

        // Find shortest path for all vertices
        for (int count = 0; count < n - 1; count++) {
            // Pick the minimum distance vertex from the set of vertices not
            // yet processed. u is always equal to src in the first iteration.
            int u = minDistance(dist, sptSet);

            // Mark the picked vertex as processed
            sptSet[u] = true;

            // Update dist value of the adjacent vertices of the picked vertex.
            for (int v = 0; v < n; v++)

                // Update dist[v] only if is not in sptSet, there is an edge from
                // u to v, and total weight of path from src to  v through u is
                // smaller than current value of dist[v]
                if (!sptSet[v] && d[u][v] && dist[u] != INT_MAX
                    && dist[u] + d[u][v] < dist[v])
                    dist[v] = dist[u] + d[u][v];
        }

        // print the constructed distance array
        for (int i = 0; i < n; i++)
            cout<<i<<" -> "<<dist[i]<<"\n";
            
            cout<<endl;
    }
}
void af2ad()
    {
        int src;
        for(int src=0;src<n;src++)
        {
        cout<<"\nSource node is " <<src<<endl;
        //cin>>src;
        int fare[n]; // The output array.  dist[i] will hold the shortest
        // distance from src to i

        bool sptSet[n]; // sptSet[i] will be true if vertex i is included in shortest
        // path tree or shortest distance from src to i is finalized

        // Initialize all distances as INFINITE and stpSet[] as false
        for (int i = 0; i < n; i++)
            fare[i] = INT_MAX, sptSet[i] = false;

        // Distance of source vertex from itself is always 0
        fare[src] = 0;

        // Find shortest path for all vertices
        for (int count = 0; count < n - 1; count++) {
            // Pick the minimum distance vertex from the set of vertices not
            // yet processed. u is always equal to src in the first iteration.
            int u = minDistance(fare, sptSet);

            // Mark the picked vertex as processed
            sptSet[u] = true;

            // Update dist value of the adjacent vertices of the picked vertex.
            for (int v = 0; v < n; v++)

                // Update dist[v] only if is not in sptSet, there is an edge from
                // u to v, and total weight of path from src to  v through u is
                // smaller than current value of dist[v]
                if (!sptSet[v] && f[u][v] && fare[u] != INT_MAX
                    && fare[u] + f[u][v] < fare[v])
                    fare[v] = fare[u] + f[u][v];
        }

        // print the constructed distance array
        for (int i = 0; i < n; i++)
            cout<<i<<" -> "<<fare[i]<<"\n";
            
            cout<<endl;
    }
}
void choice()
{
	int w;
	cout<<"Enter your choice"<<endl<<"enter 1 for minimum timing"<<endl<<"enter 2 for minimum fare\n";
	cin>>w;
	if(w==1)
	an2ad();
	if(w==2)
	af2ad();
	
}
};



int main()
{
    Graph obj;
    obj.displayAdjacencyMatrix();
    while(1)
    {
        int ch;
        cout<<"Enter 0 to exit\n";
        cout<<"Enter 1 for addition of airport\n";
        cout<<"Enter 2 for removal of airport\n";
        cout<<"Enter 3 for addition of route\n";
        cout<<"Enter 4 for removal of route\n";
        cout<<"Enter 5 for updation of route fare and distance\n";
        cout<<"Enter 6 for source to destination shortest path algorithm\n";
        cout<<"Enter 7 for single source to all nodes shortest path\n";
        cout<<"Enter 8 for all nodes to all nodes shortest path\n";
        cout<<"Enter 9 for shortest path on bases of choice by user (fare or distance)\n";
        cout<<"Enter a choice\n";
        cin>>ch;
        switch(ch)
        {
            case 0:
                cout<<"You have opted to EXIT"<<endl;
                exit(0);
            case 1:
                obj.addAirport();
                break;
            case 2:
                obj.removeAirport();
                break;
            case 3:
                obj.addRoute();
                break;
            case 6:
                obj.s2d();
                break;
            /*case 7:
                obj.s2ad();
                break;
            */case 8:
			    obj.an2ad();
			    break;
			case 9:
			    obj.choice();
			    break;    
        }
    }
    return 0;
}
