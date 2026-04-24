def analyze_histogram(image_path):
    from PIL import Image
    
    img = Image.open(image_path)
    histogram = img.histogram()
    
    #Simple check: sudden spikes or irregularities
    variation = max(histogram) - min(histogram)
    
    if variation > 20000:
        return "Highly Suspicious", 85
    elif variation >12000:
        return "Moderate Variation", 65
    else:
        return "Normal Histogram", 30