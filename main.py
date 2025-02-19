from .nodes import FloatPiecewiseRemap

NODE_CLASS_MAPPINGS = {
    "FloatPiecewiseRemap": FloatPiecewiseRemap
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FloatPiecewiseRemap": "Float Piecewise Remap"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']