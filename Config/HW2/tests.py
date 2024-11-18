import unittest
from visualizer import get_git_commit_data, build_dependency_graph, generate_plantuml_code

class TestDependencyVisualizer(unittest.TestCase):
    def test_build_dependency_graph(self):
        sample_data = {
            "commit1": ["file1", "file2"],
            "commit2": ["file2", "file3"]
        }
        graph = build_dependency_graph(sample_data)
        expected_graph = [
            '"commit1" --> "file1"',
            '"commit1" --> "file2"',
            '"commit2" --> "file2"',
            '"commit2" --> "file3"'
        ]
        self.assertEqual(graph, expected_graph)

    def test_generate_plantuml_code(self):
        sample_graph = ['"commit1" --> "file1"', '"commit2" --> "file2"']
        plantuml_code = generate_plantuml_code(sample_graph)
        self.assertTrue("@startuml" in plantuml_code)
        self.assertTrue("@enduml" in plantuml_code)
        self.assertIn('"commit1" --> "file1"', plantuml_code)

if __name__ == "__main__":
    unittest.main()
