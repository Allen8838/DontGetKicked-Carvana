# AW Comment
# Motivation for the following assumptions came from the following line of thinking:
# IsBadBuy could be due to the following factors: 
# 1. Dealer buying the wrong kind of car/at the wrong price
# 2. The car may be problematic itself due to poor manufacturing
# 3. The person selling the car may be intentionally hiding info
# 4. The environment may incentivize selling a bad car (e.g. unemployment, lax lemon laws)
# The Assumptions made below relate to #2, #3 and #4.

# Source: https://www.realcartips.com/news/1420-lemon-law-rankings.shtml
# AW Comment: Converting the grades from the website into ordinal rankings from 1-9
# Also making an assumption that these grades are applicable to the 2009-2010 period when
# these cars were purchased.
STATES_LEMON_GRADES = {'NJ': 1,
                       'WA': 1,
                       'RI': 2,
                       'HI': 2,
                       'OH': 2,
                       'NY': 2,
                       'ME': 3,
                       'FL': 3,
                       'TX': 3,
                       'DC': 3,
                       'ID': 3,
                       'CA': 3,
                       'GA': 3,
                       'WV': 3,
                       'MA': 3,
                       'MN': 3,
                       'IA': 4,
                       'NH': 4,
                       'VA': 4,
                       'CT': 4,
                       'WI': 4,
                       'AR': 4,
                       'MD': 5,
                       'VT': 5,
                       'DE': 5,
                       'NC': 5,
                       'OR': 5,
                       'SC': 6,
                       'SD': 6,
                       'IN': 7,
                       'MI': 7,
                       'MT': 7,
                       'AZ': 7,
                       'AL': 7,
                       'PA': 7,
                       'NM': 7,
                       'OK': 7,
                       'TN': 7,
                       'WY': 7,
                       'NE': 8,
                       'KY': 8,
                       'AK': 8,
                       'MS': 8,
                       'KS': 8,
                       'UT': 8,
                       'NV': 8,
                       'MO': 9,
                       'LA': 9,
                       'ND': 9,
                       'CO': 9,
                       'IL': 9
                       }


# Source: https://itspubs.ucdavis.edu/download_pdf.php?id=309, pg 73 of 179
# AW Comment: The research is from 2000. Making an assumption that these findings
# are still applicable to this 2009-2010 data. May need to do a sensitivity analysis
# to check/sanity check whether there's anything funky with using this study.
# Also bear in mind that the survey conducted in the study above were based off of SF residents.
# There may be a chance of a sampling bias if the study isn't sufficiently random.
# Self created keys
# -1 Female Proportion slightly higher
# -2 Above Average Female Population
#  1 Male Proportion slightly higher
#  4 Male Proportion dominated
SIZE_TO_GENDER_PROPORTION = {'MEDIUM': -2, # From page 73 of 179 on the link above
                            'LARGE TRUCK': 4, # Mapping this to pickup on 73 of 179 on the link above
                            'COMPACT': -2, 
                            'LARGE': 1,
                            'VAN': -2,
                            'MEDIUM SUV': -1, # Mapping this to SUV on 73 of 179 on the link above
                            'LARGE SUV': 1, # Mapping this to Large on 73 of 179 on the link above
                            'SPECIALTY': -1, # Mapping this to Sports on 73 of 179 on the link above as page 30 talks about sports specialty
                            'SPORTS': -1,
                            'CROSSOVER': -1, # Mapping this to SUV 73 of 179 on the link above as SUVs and Crossovers are considered similar
                            'SMALL SUV': -1, # Mapping this to Small on 73 of 179
                            'SMALL TRUCK': 4, # Mapping this to Pickup on 73 of 179 on the link above
                            }

# Source: https://www.automotiveaddicts.com/10154/jd-power-and-associates-2010-vehicle-dependability-study-vds
# AW Comment: Search was from Google in the custom date range of 1/1/2010 - 12/31/2010
# Better to match the year of the dependability to the year of the car but assuming that 
# Dependability doesn't change that much for now
MAKE_TO_DEPENDABILITY = {'MAZDA': 195,
                        'DODGE': 190,
                        'FORD': 141,
                        'MITSUBISHI': 202, 
                        'KIA': 167,
                        'GMC': 165,
                        'NISSAN': 180,
                        'CHEVROLET': 176, 
                        'SATURN': 164,
                        'CHRYSLER': 166,
                        'MERCURY': 121,
                        'HYUNDAI': 148,
                        'TOYOTA': 128,
                        'PONTIAC': 192,
                        'SUZUKI': 253,
                        'JEEP': 222,
                        'HONDA': 132,
                        'OLDSMOBILE': 'NA', 
                        'BUICK': 115,
                        'SCION': 201, # Same as Toyota Scion
                        'VOLKSWAGEN': 225,
                        'ISUZU': 'NA',
                        'LINCOLN': 114,
                        'MINI': 203,
                        'SUBARU': 155,
                        'CADILLAC': 150,
                        'VOLVO': 167,
                        'INFINITI': 150,
                        'PLYMOUTH': 'NA', 
                        'LEXUS': 115,
                        'ACURA': 143,
                        'TOYOTA SCION': 201,
                        'HUMMER': 169,
                         }


# Source: https://itspubs.ucdavis.edu/download_pdf.php?id=309, pg. 76 of 179
# AW Comment: The research is from 2000. Making an assumption that these findings
# are still applicable to this 2009-2010 data. May need to do a sensitivity analysis
# to check/sanity check whether there's anything funky with using this study.
# Also bear in mind that the survey conducted in the study above were based off of SF residents.
# There may be a chance of a sampling bias if the study isn't sufficiently random.
SIZE_TO_FT_PERCENT = {'MEDIUM': 62, # From page 73 of 179 on the link above
                            'LARGE TRUCK': 79, # Mapping this to pickup on 76 of 179 on the link above
                            'COMPACT': 65, 
                            'LARGE': 38,
                            'VAN': 53,
                            'MEDIUM SUV': 79, # Mapping this to SUV on 76 of 179 on the link above
                            'LARGE SUV': 38, # Mapping this to Large on 76 of 179 on the link above
                            'SPECIALTY': 71, # Mapping this to Sports on 76 of 179 on the link above as page 30 talks about sports specialty
                            'SPORTS': 71,
                            'CROSSOVER': 80, # Mapping this to SUV 76 of 179 on the link above as SUVs and Crossovers are considered similar
                            'SMALL SUV': 72, # Mapping this to Small on 76 of 179
                            'SMALL TRUCK': 79, # Mapping this to Pickup on 76 of 179 on the link above
                             }


# Source: https://itspubs.ucdavis.edu/download_pdf.php?id=309, pg. 76 of 179
# AW Comment: The research is from 2000. Making an assumption that these findings
# are still applicable to this 2009-2010 data. May need to do a sensitivity analysis
# to check/sanity check whether there's anything funky with using this study.
# Also bear in mind that the survey conducted in the study above were based off of SF residents.
# There may be a chance of a sampling bias if the study isn't sufficiently random.
SIZE_TO_PT_PERCENT = {'MEDIUM': 12, # From page 73 of 179 on the link above
                            'LARGE TRUCK': 7, # Mapping this to pickup on 76 of 179 on the link above
                            'COMPACT': 13, 
                            'LARGE': 21,
                            'VAN': 18,
                            'MEDIUM SUV': 7, # Mapping this to SUV on 76 of 179 on the link above
                            'LARGE SUV': 21, # Mapping this to Large on 76 of 179 on the link above
                            'SPECIALTY': 17, # Mapping this to Sports on 76 of 179 on the link above as page 30 talks about sports specialty
                            'SPORTS': 17,
                            'CROSSOVER': 7, # Mapping this to SUV on 76 of 179 on the link above as SUVs and Crossovers are considered similar
                            'SMALL SUV': 12, # Mapping this to Small on 76 of 179
                            'SMALL TRUCK': 7, # Mapping this to Pickup on 76 of 179 on the link above
                            }


# Source: https://itspubs.ucdavis.edu/download_pdf.php?id=309, pg. 76 of 179
# AW Comment: The research is from 2000. Making an assumption that these findings
# are still applicable to this 2009-2010 data. May need to do a sensitivity analysis
# to check/sanity check whether there's anything funky with using this study.
# Also bear in mind that the survey conducted in the study above were based off of SF residents.
# There may be a chance of a sampling bias if the study isn't sufficiently random.
SIZE_TO_UNEMPLOYED_PERCENT = {'MEDIUM': 5, # From page 73 of 179 on the link above
                            'LARGE TRUCK': 5, # Mapping this to pickup on 76 of 179 on the link above
                            'COMPACT': 8, 
                            'LARGE': 0,
                            'VAN': 16,
                            'MEDIUM SUV': 5, # Mapping this to SUV on 76 of 179 on the link above
                            'LARGE SUV': 0, # Mapping this to Large on 76 of 179 on the link above
                            'SPECIALTY': 2, # Mapping this to Sports on 76 of 179 on the link above as page 30 talks about sports specialty
                            'SPORTS': 2,
                            'CROSSOVER': 5, # Mapping this to SUV on 76 of 179 on the link above as SUVs and Crossovers are considered similar
                            'SMALL SUV': 4, # Mapping this to Small on 76 of 179
                            'SMALL TRUCK': 3, # Mapping this to Pickup on 76 of 179 on the link above
                            }



# Source: https://itspubs.ucdavis.edu/download_pdf.php?id=309, pg. 76 of 179
# AW Comment: The research is from 2000. Making an assumption that these findings
# are still applicable to this 2009-2010 data. May need to do a sensitivity analysis
# to check/sanity check whether there's anything funky with using this study.
# Also bear in mind that the survey conducted in the study above were based off of SF residents.
# There may be a chance of a sampling bias if the study isn't sufficiently random.
# Adding the above FT, PT, and U and subtracting it from 100 to get the numbers below.
# Idea is to use these numbers as the chance that a given owner may fall into one of these classes.
SIZE_TO_RETIRED_PERCENT = {'MEDIUM': 21, # From page 73 of 179 on the link above
                            'LARGE TRUCK': 9, # Mapping this to pickup on 76 of 179 on the link above
                            'COMPACT': 14, 
                            'LARGE': 41,
                            'VAN': 13,
                            'MEDIUM SUV': 9, # Mapping this to SUV on 76 of 179 on the link above
                            'LARGE SUV': 41, # Mapping this to Large on 76 of 179 on the link above
                            'SPECIALTY': 10, # Mapping this to Sports on 76 of 179 on the link above as page 30 talks about sports specialty
                            'SPORTS': 10,
                            'CROSSOVER': 8, # Mapping this to SUV on 76 of 179 on the link above as SUVs and Crossovers are considered similar
                            'SMALL SUV': 12, # Mapping this to Small on 76 of 179
                            'SMALL TRUCK': 11, # Mapping this to Pickup on 76 of 179 on the link above
                            }
