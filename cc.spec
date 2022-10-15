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
		2220.		[property MC6]
		2221.		[property MC4]
		2222.		[property MC5]
		2720.		[property MC6]
		2721.		[property MC7]
	Length:
		14.		    [if AmexTC1 || AmexTC2 || AmexTC3 || AmexTC4 || AmexTC5]
		15.		
		16.		    [property VisaLen] [property MCLen]
		17.		    [if !AmexTC1 && !AmexTC2 && !AmexTC3 && !AmexTC4 && !AmexTC5]

#	Contains only But Not Prefix and Not Other Valid:
#		4.  		[if VisaLen && not any of the prefixes]
#		52.		    [if MCLen && not any of the prefixes]
#		2222.		[if MCLen && not any of the prefixes]	