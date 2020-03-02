import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import Admin from '../Admin';

describe('Admin', () => {
  it('renders a snapshot properly', () => {
    const tree = renderer.create(<Admin />).toJSON();
    expect(tree).toMatchSnapshot();
  });

  const wrapper = shallow(<Admin />);
  it('renders properly', () => {
    const header = wrapper.find('h1');
    expect(header.text()).toBe('All Users');
  });
});
