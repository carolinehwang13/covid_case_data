# <b>Notes<b>
## <b>CSV header meanings</b>:
### <b>FIP:</b> US only. Federal Information Processing Standards code that uniquely identifies counties within the USA.
### <b>Admin2:</b> County name. US only.
### <b>Province_State:</b> Province, state or dependency name.
### <b>Country_Region:</b> Country, region or sovereignty name. The names of locations included on the Website correspond with the official designations used by the U.S. Department of State.
### <b>Last Update:</b> MM/DD/YYYY HH:mm:ss (24 hour format, in UTC).
### <b>Lat and Long_:</b> Dot locations on the dashboard. All points (except for Australia) shown on the map are based on geographic centroids, and are not representative of a specific address, building or any location at a spatial scale finer than a province/state. Australian dots are located at the centroid of the largest city in each state.
### <b>Combined_Key:</b> "County, State, US"
### <b>UID:</b>
* US by itself is 840 (UID = code3).
* US dependencies, American Samoa, Guam, Northern Mariana Islands, Virgin Islands and Puerto Rico, UID = code3. Their Admin0 FIPS codes are different from code3.
* US states: UID = 840 (country code3) + 000XX (state FIPS code). Ranging from 8400001 to 84000056.
* Out of [State], US: UID = 840 (country code3) + 800XX (state FIPS code). Ranging from 8408001 to 84080056.
* Unassigned, US: UID = 840 (country code3) + 900XX (state FIPS code). Ranging from 8409001 to 84090056.
* US counties: UID = 840 (country code3) + XXXXX (5-digit FIPS code).
* Exception type 1, such as recovered and Kansas City, ranging from 8407001 to 8407999.
* Exception type 2, Bristol Bay plus Lake Peninsula replaces Bristol Bay and its FIPS code. Population is 836 (Bristol Bay) + 1,592 (Lake and Peninsula) = 2,428 (Bristol Bay plus Lake Peninsula). 2148 (Hoonah-Angoon) + 579 (Yakutat) = 2727 (Yakutat plus Hoonah-Angoon). UID is 84002282, the same as Yakutat. New York City replaces New York County and its FIPS code. New York City popluation is calculated as Bronx (1,418,207) + Kings (2,559,903) + New York (1,628,706) + Queens (2,253,858) + Richmond (476,143) = NYC (8,336,817). (updated on Aug 31)
* Exception type 3, Diamond Princess, US: 84088888; Grand Princess, US: 84099999.
* Exception type 4, municipalities in Puerto Rico are regarded as counties with FIPS codes. The FIPS code for the unassigned category is defined as 72999.