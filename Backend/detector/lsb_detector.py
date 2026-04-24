def analyze_lsb(image_path):
    from PIL import Image
    import numpy as np
    
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img)
    
    #Extract LSB
    lsb = pixels & 1
    
    # Count zeros and ones
    zeros = np.sum(lsb == 0)
    ones = np.sum(lsb == 1)
    
    total = zeros + ones
    
    zero_ratio = zeros / total
    one_ratio = ones / total
    
    #Calculate difference
    diff = abs(zero_ratio - one_ratio)
    
    #Confidence logic
    if diff < 0.01:
        return "Highly Suspicious", 90
    elif diff < 0.03:
        return "Moderately Suspicious", 70
    elif diff <0.05:
        return "Slightly Suspicious", 50
    else:
        return "Likely Clean Image", 20
    