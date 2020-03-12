import React from 'react';
import { shallow } from 'enzyme';

import UserStatus from '../UserStatus';

const listItems = [
  { index: 0, name: 'User ID' },
  { index: 1, name: 'Email' },
  { index: 2, name: 'Active' },
  { index: 3, name: 'Admin' }
];

describe('<UserStatus />', () => {
  const wrapper = shallow(<UserStatus />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });

  it('should have a header', () => {
    expect(wrapper.find('h1').length).toBe(1);
    expect(wrapper.find('h1').text()).toBe('User Status');
  });

  const list = wrapper.find('.list-group');
  it('should have a list', () => {
    expect(list.length).toBe(1);
  });

  listItems.forEach(listItem => {
    it(`should have a ${listItem.name} list item`, () => {
      const item = list.find('.list-group-item').get(listItem.index);
      expect(item.props.children[0].props.children).toContain(listItem.name);
    });
  });
});

// Should add another test to check that the fields get populated with values
// from state when the state becomes available
