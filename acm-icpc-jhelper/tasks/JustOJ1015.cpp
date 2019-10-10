#include "../library/header.hpp"

#define INF 0x3fffffff

char g[5][5];
int mark[5][5];
int n,m;
int mi=INF;
int up[4]={1,-1,0,0};
int rl[4]={0,0,1,-1};

void dfs1(int x,int y,char tmp)
{
    mark[x][y]=1;
    for(int i=0;i<4;i++)
    {
        int tx=x+up[i];
        int ty=y+rl[i];
        if((tx>=0&&tx<n)&&(ty>=0&&ty<m)&&mark[tx][ty]==0&&g[x][y]==g[tx][ty])
        {
            dfs1(tx,ty,g[x][y]);
        }
    }
}

int min(int a, int b) {
    return a < b ? a : b;
}

void print()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
            printf("%c",g[i][j]);
        printf("\n");
    }
    printf("\n");
}

void dfs()
{
    int mark1[5][5];
    memset(mark1,0,sizeof(mark1));
    char tg[5][5];
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            tg[i][j]=g[i][j]; //记录这层的状态!
        }

    int flag,sign=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            flag=0;
            if(g[i][j]=='#') continue;
            memset(mark,0,sizeof(mark));
            if(i+1<n&&g[i][j]==g[i+1][j]&&mark1[i][j]==0)
            {
                dfs1(i,j,g[i][j]);
                flag=1;
                sign=1;
            }else
            if(i-1>=0&&g[i][j]==g[i-1][j]&&mark1[i][j]==0)
            {
                dfs1(i,j,g[i][j]);
                flag=1;
                sign=1;
            }else
            if(j+1<n&&g[i][j]==g[i][j+1]&&mark1[i][j]==0)
            {
                dfs1(i,j,g[i][j]);
                flag=1;
                sign=1;
            }else
            if(j-1>=0&&g[i][j]==g[i][j-1]&&mark1[i][j]==0)
            {
                dfs1(i,j,g[i][j]);
                flag=1;
                sign=1;
            }
            if(flag==1)
            {
                for(int i1=0;i1<n;i1++)
                    for(int j1=0;j1<m;j1++)
                        if(mark[i1][j1]==1)
                            mark1[i1][j1]=1; //代表这个区域搜索过。

                for(int i1=0;i1<n;i1++)
                {
                    for(int j1=0;j1<m;j1++)
                    {
                        if(mark[i1][j1]==1)
                        {
                            for(int k=i1-1;k>=0;k--)
                                g[k+1][j1] = g[k][j1];
                            g[0][j1]='#';
                        }
                    }
                }

                //print();

                dfs();
                //回溯
                for(int i1=0;i1<n;i1++)
                    for(int j1=0;j1<m;j1++)
                        g[i1][j1]=tg[i1][j1];

                flag=0;

                //print();
            }
        }
    }

    if(sign==0) //找不到解的情况！
    {
        int cnt=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(g[i][j]!='#')
                {
                    cnt++;
                }
            }
        mi=min(cnt,mi);
        return ;
    }

}

class JustOJ1015 {
public:
	void solve(std::istream& in, std::ostream& out) {
        int T;
        in >> T;
        TIMES(tid, T) {
            mi=INF;
            in >> n >> m;
            for(int i=0;i<n;i++) {
                in >> g[i];
            }
            dfs();
            out << mi << endl;
        }
	}
};
