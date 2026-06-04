package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func Day1() int64 {
	startt := time.Now()

	fmt.Println("Day1 start")

	data, err := os.ReadFile("data/day01.txt")

	if err != nil {
		fmt.Print(err)
		panic(err)
	}

	var pos int = 50
	var resp1 int
	var resp2 int

	for _, line := range strings.Split(string(data), "\n") {
		value, _ := strconv.Atoi(line[1:])

		complete := value / 100
		rest := value - (complete * 100)

		resp2 += complete

		if line[0] == 'L' {
			if rest > pos && pos != 0 {
				resp2++
			}
			pos = pos + 100 - rest
		} else {
			pos += rest
			if pos > 100 {
				resp2++
			}
		}

		pos %= 100

		if pos == 0 {
			resp1++
			resp2++
		}
	}

	dt := time.Since(startt)

	fmt.Println("Part 1:", resp1)
	fmt.Println("Part 2:", resp2)
	fmt.Println("Run time:", dt.Microseconds())
	return dt.Microseconds()
}
