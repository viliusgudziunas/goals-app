import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import About from '../About';

describe('About', () => {
  it('renders a snapshot properly', () => {
    const tree = renderer.create(<About />).toJSON();
    expect(tree).toMatchSnapshot();
  });

  const wrapper = shallow(<About />);
  it('renders properly', () => {
    const header = wrapper.find('h1');
    expect(header.text()).toBe('About');

    const paragraph = wrapper.find('p');
    expect(paragraph.text()).toBe('Add something relevant here');
  });
});
