var c = console;

funtion Map(f,a)
{
    var ma = [];
    for(var i in a){
        ma.push(f(a[i]));
    }
    return ma;
}

function square(x)
{
    return x*x;
}

c.log("map(x^2,[3,1,5,4,2])="+Map(square,[3,1,5,4,2]));
c.log("map(sin(x),[3,1,5,4,2])="+Map(math.sin,[3,1,5,4,2]));