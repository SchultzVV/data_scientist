import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from ds_workflow.feature_store import build_feature_pipeline
from ds_workflow.deploy import simulate_canary


def test_build_feature_pipeline():
    pipeline = build_feature_pipeline(k=5)
    assert len(pipeline.steps) == 2
    assert [name for name, _ in pipeline.steps] == ["scale", "select"]


def test_simulate_canary_pass():
    metric, ok = simulate_canary(0.5, 0.6)
    assert ok
    assert metric == 0.6
