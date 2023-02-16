## GeoMask

Training supervised machine learning/deep learning models requires large annotated datasets. Creating up to date masks for satelllite data can be a difficult task as the base maps for services like [GeoJSON.io](https://geojson.io/#map=2/0/20) or [GeoMan.io](https://geoman.io/geojson-editor) are not up to date.
[GeoMask]() allows a user to upload tiff files downloaded from [EO Browser](https://apps.sentinel-hub.com/eo-browser/) which will be automatically overlaid on top of a map. All you need to do next is to create polygons, and hit export to download the masks.

### How to use
1. Download true color image from [EO Browser](https://apps.sentinel-hub.com/eo-browser/)
2. Upload the true color image by browsing its location on your local system.
3. Create polygons/rectangles on the areas you want to unmask.
4. Hit on export to download the data.