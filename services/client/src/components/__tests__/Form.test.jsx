import React from 'react';
import { shallow } from 'enzyme';

import Form from '../Form';

const forms = [
  { type: 'Register', title: 'Register' },
  { type: 'Login', title: 'Log In' }
];

forms.forEach(formInfo => {
  describe(`${formInfo.title} <Form />`, () => {
    const wrapper = shallow(<Form formType={formInfo.type} />);
    it('should match the snapshot', () => {
      expect(wrapper.html()).toMatchSnapshot();
    });

    it('should have a header', () => {
      expect(wrapper.find('h1').length).toBe(1);
      expect(wrapper.find('h1').get(0).props.children).toBe(formInfo.title);
    });

    const form = wrapper.find('form');
    it('should have a form', () => {
      expect(form.length).toBe(1);
    });

    const formFields = form.find('input');
    it('should have two input fields', () => {
      expect(formFields.length).toBe(2);
    });

    it('should have email field', () => {
      expect(formFields.get(0).props.type).toBe('email');
      expect(formFields.get(0).props.value).toBe('');
    });

    it('should have password field', () => {
      expect(formFields.get(1).props.type).toBe('password');
      expect(formFields.get(1).props.value).toBe('');
    });

    it('should have a submit button', () => {
      expect(form.find('button').length).toBe(1);
      expect(form.find('button').get(0).props.type).toBe('submit');
    });
  });
});
