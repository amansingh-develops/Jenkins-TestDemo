#!/usr/bin/env python3
"""
Automated Test Suite for HTML Registration Form
Tests the presence and attributes of the form and required input fields:
  - Form element (<form>)
  - Name input field
  - Email input field
  - Contact Number input field
  - Submit button
Uses only the Python standard library so it runs without external dependencies.
"""

import os
import sys
import unittest
from html.parser import HTMLParser


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []
        self.labels = []
        self._current_tag = None

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self._current_tag = tag

        if tag == 'form':
            self.forms.append(attr_dict)
        elif tag == 'input':
            self.inputs.append(attr_dict)
        elif tag == 'button':
            self.buttons.append(attr_dict)
        elif tag == 'label':
            self.labels.append(attr_dict)


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html_path = os.path.join(os.path.dirname(__file__), 'index.html')
        cls.file_exists = os.path.exists(cls.html_path)
        cls.parser = FormParser()

        if cls.file_exists:
            with open(cls.html_path, 'r', encoding='utf-8') as f:
                content = f.read()
            cls.parser.feed(content)

    def test_01_html_file_exists(self):
        """Verify that index.html exists in the repository root."""
        self.assertTrue(self.file_exists, f"File index.html not found at {self.html_path}")

    def test_02_form_element_exists(self):
        """Verify that the <form> element is present in the HTML."""
        self.assertGreater(
            len(self.parser.forms), 0,
            "No <form> tag found in index.html"
        )

    def test_03_name_field_exists(self):
        """Verify that the Name input field is present with appropriate attributes."""
        name_inputs = [
            inp for inp in self.parser.inputs 
            if inp.get('name') == 'name' or inp.get('id') == 'name' or 'name' in inp.get('placeholder', '').lower()
        ]
        self.assertGreater(
            len(name_inputs), 0,
            "Input field for 'Name' was not found in the form."
        )
        field = name_inputs[0]
        self.assertIn(field.get('type', 'text').lower(), ['text'], "Name field should have type='text'")

    def test_04_email_field_exists(self):
        """Verify that the Email input field is present with appropriate attributes."""
        email_inputs = [
            inp for inp in self.parser.inputs 
            if inp.get('type') == 'email' or inp.get('name') == 'email' or inp.get('id') == 'email'
        ]
        self.assertGreater(
            len(email_inputs), 0,
            "Input field for 'Email' was not found in the form."
        )
        field = email_inputs[0]
        self.assertEqual(field.get('type', '').lower(), 'email', "Email field should have type='email'")

    def test_05_contact_number_field_exists(self):
        """Verify that the Contact Number input field is present with appropriate attributes."""
        contact_inputs = [
            inp for inp in self.parser.inputs 
            if inp.get('name') in ['contact', 'phone', 'mobile'] or 
               inp.get('id') in ['contact', 'phone', 'mobile'] or
               inp.get('type') == 'tel' or
               'contact' in inp.get('placeholder', '').lower() or
               'phone' in inp.get('placeholder', '').lower()
        ]
        self.assertGreater(
            len(contact_inputs), 0,
            "Input field for 'Contact Number' was not found in the form."
        )

    def test_06_submit_button_exists(self):
        """Verify that a Submit button is present in the form."""
        submit_buttons = [
            b for b in self.parser.buttons if b.get('type') == 'submit' or b.get('id') == 'submit'
        ]
        submit_inputs = [
            inp for inp in self.parser.inputs if inp.get('type') == 'submit' or inp.get('id') == 'submit'
        ]
        total_submit = len(submit_buttons) + len(submit_inputs)
        self.assertGreater(
            total_submit, 0,
            "No Submit button (<button type='submit'> or <input type='submit'>) was found."
        )


if __name__ == '__main__':
    print("=" * 60)
    print(" RUNNING AUTOMATED HTML FORM VALIDATION TESTS")
    print("=" * 60)
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHTMLForm)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print(f" ALL TESTS PASSED: {result.testsRun}/{result.testsRun} checks succeeded.")
        print("=" * 60)
        sys.exit(0)
    else:
        print(f" TESTS FAILED: {len(result.failures)} failures, {len(result.errors)} errors.")
        print("=" * 60)
        sys.exit(1)
