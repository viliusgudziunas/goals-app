import React from 'react';
import { shallow } from 'enzyme';

import LoginPage from '../LoginPage';

describe('<LoginPage />', () => {
  const wrapper = shallow(<LoginPage />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });
});

describe('When not authenticated, <LoginPage />', () => {
  const wrapper = shallow(<LoginPage />);
  it("should render a <Form /> with type 'Login'", () => {
    expect(wrapper.find('Form').length).toBe(1);
    expect(wrapper.find('Form').prop('formType')).toBe('Login');
  });
});

// describe('When authenticated, <LoginPage />', () => {
//   const wrapper = shallow(<LoginPage />);
//   it('should redirect to "/"', () => {});
// });
