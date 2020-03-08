import React from 'react';
import { shallow } from 'enzyme';

import RegisterPage from '../RegisterPage';

describe('<RegisterPage />', () => {
  const wrapper = shallow(<RegisterPage />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });
});

describe('When not authenticated, <RegisterPage />', () => {
  const wrapper = shallow(<RegisterPage />);
  it("should render a <Form /> with type 'Register'", () => {
    expect(wrapper.find('Form').length).toBe(1);
    expect(wrapper.find('Form').prop('formType')).toBe('Register');
  });
});

// describe('When authenticated, <RegisterPage />', () => {
//   const wrapper = shallow(<RegisterPage />);
//   it('should redirect to "/"', () => {});
// });
