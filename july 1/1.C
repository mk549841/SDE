#include<bits/stdc++.h>
using namespace std;
long long MOD = 1e9+7;

struct child
{
int storybooks, toys, rollNum;
};

bool cmp(child c1, child c2)
{
if(c1.toys == c2.toys)
{
if(c1.storybooks == c2.storybooks)
return c1.rollNum > c2.rollNum;
return c1.storybooks >
c2.storybooks;
}
return c1.toys < c2.toys;
}

int main()
{
int t;
int n;
cin>>n;
vector<child> children(n);
for(int i=0;i<n;i++)
{
cin>>children[i].storybooks>>children[i].toys;
children[i].rollNum = i+1;
}
sort(children.begin(),children.end(),cmp);
for(int i=0;i<n;i++)
cout<<children[i].rollNum<<" ";
return 0;
}
