import React from 'react';
import { shallow } from 'enzyme';

import Admin from '../Admin';

describe('<Admin />', () => {
  const wrapper = shallow(<Admin />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });

  it('should have a header', () => {
    expect(wrapper.find('h1').length).toBe(1);
    expect(wrapper.find('h1').text()).toBe('All Users');
  });
});
