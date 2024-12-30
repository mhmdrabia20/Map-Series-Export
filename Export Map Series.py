import arcpy.mp

# Set up the map series parameters
map_series_name = "barcodes"  # Name of your map series
output_folder = r"C:\Users\user\Desktop\barcode"  # Path to the output folder where PNG images will be saved
output_name_prefix = ""  # Prefix for the output PNG files

# Specify the desired page numbers to export
desired_page_numbers = [36

]

# Reference the project and map series
project = arcpy.mp.ArcGISProject("CURRENT")  # Use "CURRENT" to reference the current project
layout = project.listLayouts(map_series_name)[0]  # Get the layout by name
map_series = layout.mapSeries

# Export specified pages in the map series to PNG
for pageNum in desired_page_numbers:
    if pageNum > 0 and pageNum <= map_series.pageCount:
        map_series.currentPageNumber = pageNum
        output_name = f"{output_name_prefix}{pageNum}"
        output_path = f"{output_folder}\\{output_name}.png"
        layout.exportToPNG(output_path, resolution=100)
        print(f"Exported page {pageNum} to {output_path}")
        
print("خلصت ي باشا")





