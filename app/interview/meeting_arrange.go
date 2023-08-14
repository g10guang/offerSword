package main

// meetingArrange 安排
func meetingArrange(alice, bob [][2]int, duration int) [2]int {
	calDurationFn := func(t [2]int) int {
		v := t[1] - t[0]
		if v < 0 {
			return -v
		}
		return v
	}

	a, b := 0, 0

	for a < len(alice) && b < len(bob) {
		if calDurationFn(alice[a]) < duration {
			a++
			continue
		}

		if calDurationFn(bob[b]) < duration {
			b++
			continue
		}

		if alice[a][0] >= bob[b][1] {
			b++
			continue
		}

		if bob[b][0] >= alice[a][1] {
			a++
			continue
		}

		maxStart := alice[a][0]
		minEnd := alice[a][1]
		if maxStart < bob[b][0] {
			maxStart = bob[b][0]
		}
		if minEnd > bob[b][1] {
			minEnd = bob[b][1]
		}

		if minEnd-maxStart < duration {
			if alice[a][0] < bob[b][0] {
				a++
			} else {
				b++
			}
			continue
		}

		min := alice[a][0]
		if min < bob[b][0] {
			min = bob[b][0]
		}

		return [2]int{min, min + duration}
	}

	return [2]int{-1, -1}
}
