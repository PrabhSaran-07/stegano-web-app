def analyze_histogram(image_path):
    from PIL import Image
    
    img = Image.open(image_path)
    histogram = img.histogram()
    
    #Simple check: sudden spikes or irregularities
    variation = max(histogram) - min(histogram)
    
    if variation > 30000:
        return "Highly Suspicious", 85
    elif variation >18000:
        return "Moderate Variation", 60
    elif variation >10000:
        return "Slight Variation", 40
    else:
        return "Normal Histogram", 15