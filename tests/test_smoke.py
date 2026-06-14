def test_runtime_dependencies_import():
    import pandas as pd
    import pyspark

    assert pd is not None
    assert pyspark is not None
