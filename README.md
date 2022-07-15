## INSAT3D Imagen

INSAT 3D image generator.

Processes INSAT HDF file and generates satellite images.

![INSAT 3D Imagen demo](https://github.com/rupeshs/insat3d_imagen/blob/main/outputs/insat3d_imagen.jpg)


8 types of image outputs supported:
- Visible channel
- Shortwave Infrared Channel
- Middle wave Infrared Channel
- Thermal Infrared Channel 1
- Thermal Infrared Channel 2
- Water Vapor Channel
- RGB composite (Day time microphysics)
- RGB composite (Night time microphysics)

Thanks [MOSDAC ISRO](https://mosdac.gov.in/) for providing the satellite data.

Satellite data can requested through MOSDAC web site.Create an account in MOSDAC and after getting the approval you can download the data.

### Dependencies

- Python (3.10)
- poetry
- Pillow
- h5py
- numpy

## References 

<a id="1" href="http://satellite.imd.gov.in/dynamic/INSAT3D_Catalog.pdf">INSAT3D Catalog </a> 

<a id="2" href="https://www.mosdac.gov.in/docs/INSAT3D_Products.pdf">INSAT-3D Data Products Format Document,Version 1.1, February 2014</a> 

<a id="3" href="https://mausam.imd.gov.in/imd_latest/contents/pdf/forecasting_sop.pdf">Standard Operation Procedure - Weather
Forecasting and Warning Services</a> 

