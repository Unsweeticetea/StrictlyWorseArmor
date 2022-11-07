# StrictlyWorseArmor
Sorts for any strictly worse armor when given a Destiny Item Manager armor export. The script doesn't sort any class items, exotics, or armor with tags so that it doesn't fill with infusion fodder. It does not consider Mobility for non-hunter armor.

Armor_Marker.exe is found in the dist folder.

Steps:
1. Take a .csv export of your DIM armor (Settings, scroll to the bottom, click "Armor" under Inventory Spreadsheets)
2. Place that .csv in the same folder as Armor_Marker.exe
3. Run the Armor_Marker.exe
4. Compare listed item IDs and delete strictly worse armor
5. Close the program

You can filter the IDs in DIM with "Id:XYZ" and mark them for deletion.
