import unittest
import tkinter as tk
from FinalProject_stageTwo import (
    Steve, Sonic, Snake, Game_and_Watch, ROB, Pyra_Mythra,
    Kazuya, Diddy_Kong, Minmin, Fox, CHARACTER_LIST,CharacterFactory
)

class TestCharacters(unittest.TestCase):

    def test_steve_stage(self):
        s = Steve()
        self.assertEqual(s.get_best_stage(), "Small Battlefield (SBF)")

    def test_sonic_stage(self):
        c = Sonic()
        self.assertEqual(c.get_best_stage(), "Town & City")

    def test_snake_stage(self):
        c = Snake()
        self.assertEqual(c.get_best_stage(), "Hollow Bastion")

    def test_gaw_stage(self):
        c = Game_and_Watch()
        self.assertEqual(c.get_best_stage(), "Hollow Bastion")

    def test_rob_stage(self):
        c = ROB()
        self.assertEqual(c.get_best_stage(), "Kalos Pokemon League (Kalos)")

    def test_pyra_mythra_stage(self):
        c = Pyra_Mythra()
        self.assertEqual(c.get_best_stage(), "Town & City")

    def test_kazuya_stage(self):
        c = Kazuya()
        self.assertEqual(c.get_best_stage(), "Final Destination (FD)")

    def test_diddy_stage(self):
        c = Diddy_Kong()
        self.assertEqual(c.get_best_stage(), "Kalos Pokemon League (Kalos)")

    def test_minmin_stage(self):
        c = Minmin()
        self.assertEqual(c.get_best_stage(), "Smashville")

    def test_fox_stage(self):
        c = Fox()
        self.assertEqual(c.get_best_stage(), "Pokemon Stadium 2 (PS2)")

    def test_each_reason_not_empty(self):
        characters = [
            Steve(), Sonic(), Snake(), Game_and_Watch(), ROB(), Pyra_Mythra(),
            Kazuya(), Diddy_Kong(), Minmin(), Fox()
        ]
        for c in characters:
            self.assertTrue(len(c.get_reason()) > 0)

class TestCharacterFactoryCLI(unittest.TestCase):

    def test_factory_returns_correct_classes(self):
        self.assertIsInstance(CharacterFactory.find_character("steve"), Steve)
        self.assertIsInstance(CharacterFactory.find_character("Sonic"), Sonic)
        self.assertIsInstance(CharacterFactory.find_character("snaKE"), Snake)
        self.assertIsInstance(CharacterFactory.find_character("g&w"), Game_and_Watch)
        self.assertIsInstance(CharacterFactory.find_character("rob"), ROB)
        self.assertIsInstance(CharacterFactory.find_character("pyra"), Pyra_Mythra)
        self.assertIsInstance(CharacterFactory.find_character("mythra"), Pyra_Mythra)
        self.assertIsInstance(CharacterFactory.find_character("kazuya"), Kazuya)
        self.assertIsInstance(CharacterFactory.find_character("diddy kong"), Diddy_Kong)
        self.assertIsInstance(CharacterFactory.find_character("minmin"), Minmin)
        self.assertIsInstance(CharacterFactory.find_character("fox"), Fox)

    def test_factory_invalid_character(self):
        with self.assertRaises(ValueError):
            CharacterFactory.find_character("mario")

class TestCharacterFactoryGUI(unittest.TestCase):

    def test_character_list_not_empty(self):
        """Ensure the character list is loaded."""
        self.assertTrue(len(CHARACTER_LIST) > 0)

    def test_find_character_valid(self):
        """Should return a Character object for a valid name."""
        name = CHARACTER_LIST[0]  # take first character from your list
        fighter = CharacterFactory.find_character(name)
        self.assertEqual(fighter.character_name, name)

    def test_find_character_case_insensitive(self):
        """Ensure search works regardless of letter case."""
        name = CHARACTER_LIST[0]
        mixed_case = name.lower()
        fighter = CharacterFactory.find_character(mixed_case)
        self.assertEqual(fighter.character_name.lower(), mixed_case)

    def test_find_character_invalid(self):
        """Ensure invalid character names raise ValueError."""
        with self.assertRaises(ValueError):
            CharacterFactory.find_character("NotARealCharacter")

    def test_character_has_best_stage(self):
        """Each character should produce a stage."""
        name = CHARACTER_LIST[0]
        fighter = CharacterFactory.find_character(name)
        stage = fighter.get_best_stage()
        self.assertIsInstance(stage, str)
        self.assertTrue(len(stage) > 0)

    def test_character_has_reason(self):
        """Each character should produce a reason string."""
        name = CHARACTER_LIST[0]
        fighter = CharacterFactory.find_character(name)
        reason = fighter.get_reason()
        self.assertIsInstance(reason, str)
        self.assertTrue(len(reason) > 0)


class TestGUIImport(unittest.TestCase):

    def test_gui_import(self):
        """Just verifies the GUI file imports without errors."""
        import SmashGUI  # <-- change to your actual filename
        self.assertTrue(True)

    def test_gui_initializes(self):
        """Smoke test for GUI creation."""
        root = tk.Tk()
        root.withdraw()
        try:
            import SmashGUI
            gui = SmashGUI.SmashGUI(root)
        except Exception as e:
            self.fail(f"GUI failed to initialize: {e}")
        finally:
            root.destroy()

if __name__ == "__main__":
    unittest.main()