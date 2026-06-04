package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func Day2() int64 {
	startt := time.Now()

	fmt.Println("Day2 start")

	// data, err := os.ReadFile("data/day02_test01.txt")
	data, err := os.ReadFile("data/day02.txt")

	if err != nil {
		fmt.Println("Error reading file", err)
		panic(err)
	}

	// Single line of data
	line := string(data)

	var resp1 int
	var resp2 int
	var nlen int

	kEXPONENT := [8]int{0, 10, 100, 1000, 10000, 100000, 1000000, 10000000}

	for _, chunk := range strings.Split(line, ",") {
		dash := strings.Index(chunk, "-")
		nstart, _ := strconv.Atoi(chunk[:dash])
		nend, _ := strconv.Atoi(chunk[dash+1:])

		for n := nstart; n <= nend; n++ {

			// Get how many digits there is in the number
			// This could be done with : math.Log10(n)+1
			// But the switch is way faster, 2+x faster
			// nlen = int(math.Log10(float64(n))) + 1
			// from the data, max nlen will be 10
			switch {
			case n >= 1000000000:
				nlen = 10
			case n >= 100000000:
				nlen = 9
			case n >= 10000000:
				nlen = 8
			case n >= 1000000:
				nlen = 7
			case n >= 100000:
				nlen = 6
			case n >= 10000:
				nlen = 5
			case n >= 1000:
				nlen = 4
			case n >= 100:
				nlen = 3
			case n >= 10:
				nlen = 2
			default:
				nlen = 1
			}

			maxpattern := nlen / 2

			// try all patterns from large to small
			for plen := maxpattern; plen >= 1; plen-- {

				// Check if pattern fits into the number
				if nlen%plen != 0 {
					continue
				}

				work := n
				divisor := kEXPONENT[plen]
				pattern := work % divisor
				work /= divisor

				for work > 0 {
					subpattern := work % divisor
					if subpattern == pattern {
						work /= divisor
					} else {
						break
					}
				}

				if work == 0 {
					resp2 += n
					if plen == maxpattern && ((plen << 1) == nlen) {
						resp1 += n
					}
					break
				}
			}
		}
	}

	dt := time.Since(startt)

	fmt.Println("Part 1:", resp1)
	fmt.Println("Part 2:", resp2)
	fmt.Println("Run time:", dt.Microseconds())
	return dt.Microseconds()
}
