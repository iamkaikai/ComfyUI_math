class FloatPiecewiseRemap:
    CATEGORY = "Custom/Math"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.5}),
                # Interval 1: e.g. map current 1 to 0.6 -> new 1 to 0.9
                "cur_min_1": ("FLOAT", {"default": 1.0}),
                "cur_max_1": ("FLOAT", {"default": 0.6}),
                "new_min_1": ("FLOAT", {"default": 1.0}),
                "new_max_1": ("FLOAT", {"default": 0.9}),
                # Interval 2: e.g. map current 0.6 to 0.4 -> new 0.9 to 0.8
                "cur_min_2": ("FLOAT", {"default": 0.6}),
                "cur_max_2": ("FLOAT", {"default": 0.4}),
                "new_min_2": ("FLOAT", {"default": 0.9}),
                "new_max_2": ("FLOAT", {"default": 0.8}),
                # Interval 3 e.g. map current 0.4 to 0.3 -> new 0.8 to 0.7
                "cur_min_3": ("FLOAT", {"default": 0.4}),
                "cur_max_3": ("FLOAT", {"default": 0.3}),
                "new_min_3": ("FLOAT", {"default": 0.8}),
                "new_max_3": ("FLOAT", {"default": 0.7}),
                # Interval 4 e.g. map current 0.3 to 0.2 -> new 0.7 to 0.4
                "cur_min_4": ("FLOAT", {"default": 0.3}),
                "cur_max_4": ("FLOAT", {"default": 0.2}),
                "new_min_4": ("FLOAT", {"default": 0.7}),
                "new_max_4": ("FLOAT", {"default": 0.4}),
                # Interval 5 e.g. map current 0.2 to 0.1 -> new 0.5 to 0.4
                "cur_min_5": ("FLOAT", {"default": 0.2}),
                "cur_max_5": ("FLOAT", {"default": 0.1}),
                "new_min_5": ("FLOAT", {"default": 0.5}),
                "new_max_5": ("FLOAT", {"default": 0.3}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "remap_value"

    def remap_value(
        self, value,
        cur_min_1, cur_max_1, new_min_1, new_max_1,
        cur_min_2, cur_max_2, new_min_2, new_max_2,
        cur_min_3, cur_max_3, new_min_3, new_max_3,
        cur_min_4, cur_max_4, new_min_4, new_max_4,
        cur_min_5, cur_max_5, new_min_5, new_max_5
    ):
        # Define the intervals as a list of tuples: (current_min, current_max, new_min, new_max)
        intervals = [
            (cur_min_1, cur_max_1, new_min_1, new_max_1),
            (cur_min_2, cur_max_2, new_min_2, new_max_2),
            (cur_min_3, cur_max_3, new_min_3, new_max_3),
            (cur_min_4, cur_max_4, new_min_4, new_max_4),
            (cur_min_5, cur_max_5, new_min_5, new_max_5)
        ]
        
        # Check each interval to see if 'value' lies within the current range.
        # This supports both ascending and descending ranges.
        for (cmin, cmax, nmin, nmax) in intervals:
            if cmin < cmax:
                if value >= cmin and value <= cmax:
                    t = (value - cmin) / (cmax - cmin)
                    return (nmin + t * (nmax - nmin),)
            else:
                # For descending intervals (e.g. 1.0 to 0.6)
                if value <= cmin and value >= cmax:
                    t = (value - cmin) / (cmax - cmin)  # denominator is negative but t still in [0,1]
                    return (nmin + t * (nmax - nmin),)
        
        # If the value doesn't fall into any interval, return it unchanged.
        return (value,)