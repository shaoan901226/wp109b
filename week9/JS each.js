function each (a,f)
{
    for(var i in a)
    {
        f(a[i]);
    }
}
each([3,4,5,6],console.log);