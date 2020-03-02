import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import AddUser from '../AddUser';

const pingFetchUsers = true;
const setPingFetchUsers = jest.fn();

describe('AddUser', () => {
  it('renders a snapshot properly', () => {
    const tree = renderer
      .create(
        <AddUser
          pingFetchUsers={pingFetchUsers}
          setPingFetchUsers={setPingFetchUsers}
        />
      )
      .toJSON();
    expect(tree).toMatchSnapshot();
  });

  const wrapper = shallow(
    <AddUser
      pingFetchUsers={pingFetchUsers}
      setPingFetchUsers={setPingFetchUsers}
    />
  );
  it('renders properly', () => {
    const form = wrapper.find('form');

    expect(form.find('input').length).toBe(1);
    expect(form.find('input').get(0).props.type).toBe('email');
    expect(form.find('button').get(0).props.type).toBe('submit');
  });
});
