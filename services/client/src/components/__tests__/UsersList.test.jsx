import React from 'react';
import { shallow } from 'enzyme';

import UsersList from '../UsersList';

const headers = [
  { index: 0, name: 'ID' },
  { index: 1, name: 'Email' },
  { index: 2, name: 'Active' },
  { index: 3, name: 'Admin' }
];

describe('<UsersList />', () => {
  const wrapper = shallow(<UsersList />);
  it('should match the snapshot', () => {
    expect(wrapper.html()).toMatchSnapshot();
  });

  it('should have a header', () => {
    expect(wrapper.find('h1').length).toBe(1);
    expect(wrapper.find('h1').text()).toBe('All Users');
  });

  const table = wrapper.find('table');
  it('should have a table', () => {
    expect(table.length).toBe(1);
  });

  const thead = table.find('thead');
  it(`should have a table head`, () => {
    expect(thead.length).toBe(1);
  });

  headers.forEach(header => {
    it(`should have a header column ${header.name}`, () => {
      expect(thead.find('th').get(header.index).props.children).toBe(
        header.name
      );
    });
  });

  it(`should have a table body`, () => {
    const tbody = table.find('tbody');
    expect(tbody.length).toBe(1);
  });
});

// Needs a test where I add a user and then check that the table body
// is displayed correctly
