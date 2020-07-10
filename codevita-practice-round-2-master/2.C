#include<bits/stdc++.h>
using namespace std;
int main()
{
int t;
cin>>t;
while(t--)
{
    long long int n;
    cin>>n;
    long long int a[n],b[n];
    for(int i=0;i<n;i++)
    {
    cin>>a[i]>>b[i];
    }
    sort(a,a+n);
    sort(b,b+n);
    long long int l1=a[n-1]-a[0];
    long long int b1=b[n-1]-b[0];
    l1=max(l1,b1);
    cout<<l1*l1<<endl;
    }
}
