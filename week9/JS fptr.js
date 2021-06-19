funtion sub(a,b)
{
    return a-b;
}

funtion f5(f,a)
{
    return f(a,5);
}

console.log("(8,5)"=+sub(8,5));
console.log("f5(sub,8)"=+sub(sub,8));