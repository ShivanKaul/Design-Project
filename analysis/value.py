from scipy.interpolate import InterpolatedUnivariateSpline as pi 

def intervalues (mylistx, mylisty, mylistom):
	i = 1.0 
	a = []
	while i < len(mylistom):
		a.append(i)
		i = i+1.0
	function = pi(mylistx, mylisty)
	return function.__call__(a).tolist()	
