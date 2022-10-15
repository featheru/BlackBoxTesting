#TSL Generator File for CreditCard Spec
#10/15/22

#CreditCard
	Prefix:	
		4.	   	    [property VisaTC1]
		33.		    [property AmexTC1]	
		34.		    [property AmexTC2]	
		36.		    [property AmexTC3]
		37.		    [property AmexTC4]
		38.		    [property AmexTC5]
		50.		    [property MC1]
		51.		    [property MC2]
		52.		    [property MC3]
		55.		    [property MC4]
		56.		    [property MC5]
		2220.		[property MC11]
		2221.		[property MC12]
		2222.		[property MC13]
		2720.		[property MC14]
		2721.		[property MC15]
	Length:
		14.		    [if AmexTC2 || AmexTC4]
		15.		    [if !MC1 && !MC5 && !MC11 && !MC15]
		16.		    [if !AmexTC1 && !AmexTC3 && !AmexTC5]
		17.		    [if !AmexTC1 && !AmexTC2 && !AmexTC3 && !AmexTC4 && !AmexTC5 && !MC1 && !MC5 && !MC11 && !MC15]

#	Contains only But Not Prefix and Not Other Valid:
#		4.  		[if VisaLen && not any of the prefixes] --> 04444....
#		52.		    [if MCLen && not any of the prefixes] --> 0525252....
#		2222.		[if MCLen && not any of the prefixes] --> 02222222222...
#       34.         [if AmexLen && not any of the prefixes]
#       37.         [if AmexLen && not any of the prefixes]