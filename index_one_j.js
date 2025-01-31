function narcissistic(value){
    let convertSTR=value.toString()
    let lening=convertSTR.length 
    let sum= 0
    for (let i=0 ; i < lening ; i++)
        sum += Number(convertSTR[i]) ** lening
    if(sum === value){
        console.log('true') 
    }else{
        console.log('false')
    }

}
narcissistic()