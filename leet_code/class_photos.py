def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort()
	blueShirtHeights.sort()

	maxArray = []
	minArray = []
	
	if redShirtHeights[0] > blueShirtHeights[0]:
		maxArray = redShirtHeights
		minArray = blueShirtHeights
	else:
		maxArray = blueShirtHeights
		minArray = redShirtHeights
		
	for i in range(len(maxArray)):
		if maxArray[i] <= minArray[i]:
			return False

	return True