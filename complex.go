package main

import "fmt"
import "math"
import "math/cmplx"

func zn(n float64) complex128{
	var zn complex128 = cmplx.Exp(complex(0.0, n))
	return zn
}

func main(){
	var size float64
	fmt.Print("Enter size of array: ")
	fmt.Scanln(&size)
	var g = make([]float64, int(size))
	g[0] = 1.
	k := 1.
	for n := 0.0; n<size - 1; n++{
		var m = g[int(n)]
		var small = math.Min(cmplx.Abs(zn(m) - 1), 1/(n+1))
		for cmplx.Abs(zn(k) - 1) >= small{
			k += 1
		}
		g[int(n) + 1] = k
		fmt.Println(k)
	}
	fmt.Println(g)
	for i,s := range g{
		fmt.Println(i, zn(s))
	}
}
