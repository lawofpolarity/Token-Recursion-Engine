import unittest
from src.token_recursion_engine import TokenRecursionEngine, deterministic_demo_vector

class TREMTests(unittest.TestCase):
    def test_deepest_local_layer_wins(self):
        e=TokenRecursionEngine(3);e.store_local(0,"k","shallow");e.store_local(2,"k","deep")
        r=e.retrieve("k");self.assertEqual(r.summary,"deep");self.assertEqual(r.level,2);self.assertEqual(r.provenance,"LOCAL")

    def test_external_result_preserves_provenance_when_cached(self):
        e=TokenRecursionEngine(2,external_fetch=lambda k:{"summary":"external"})
        r=e.retrieve("k");self.assertEqual(r.provenance,"EXTERNAL")
        cached=e.retrieve("k");self.assertEqual(cached.provenance,"EXTERNAL")

    def test_synthetic_is_explicit_and_not_persisted(self):
        e=TokenRecursionEngine()
        r=e.retrieve("missing");self.assertEqual(r.provenance,"SYNTHETIC")
        self.assertIsNone(e.retrieve_local("missing"))

    def test_synthetic_can_be_denied(self):
        self.assertIsNone(TokenRecursionEngine().retrieve("x",allow_synthetic=False))

    def test_demo_vector_is_deterministic(self):
        self.assertEqual(deterministic_demo_vector("abc"),deterministic_demo_vector("abc"))

    def test_invalid_depth_and_level_fail(self):
        with self.assertRaises(ValueError):TokenRecursionEngine(0)
        e=TokenRecursionEngine(2)
        with self.assertRaises(IndexError):e.store_local(2,"x","y")

if __name__=="__main__":unittest.main()
