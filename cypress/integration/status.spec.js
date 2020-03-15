import faker from 'faker';

const email = faker.internet.email();
const password = faker.internet.password();

describe('Status', () => {
  it('should not display user info is a user is not logged in', () => {
    cy.visit('/status')
      .get('h1')
      .contains('Not Allowed')

      .get('p')
      .contains('You must be logged in to view this')

      .get('a')
      .contains('User Status')
      .should('not.be.visible')

      .get('a')
      .contains('Log Out')
      .should('not.be.visible')

      .get('a')
      .contains('Register')

      .get('a')
      .contains('Log In');
  });

  it('should display user info is a user is logged in', () => {
    // register user
    cy.visit('/register')
      .get('input[name="email"]')
      .type(email)

      .get('input[name="password"]')
      .type(password)

      .get('button[type="submit"]')
      .click();

    // assert "/status" is displayed properly
    cy.contains('All Users');

    cy.get('a')
      .contains('User Status')
      .click();

    cy.get('.list-group-item > strong')
      .contains('User ID:')

      .get('.list-group-item > strong')
      .contains('Email:')

      .get('.list-group-item')
      .contains(email)

      .get('.list-group-item > strong')
      .contains('Active:')

      .get('.list-group-item > strong')
      .contains('Admin:');

    cy.get('a')
      .contains('User Status')

      .get('a')
      .contains('Log Out')

      .get('a')
      .contains('Register')
      .should('not.be.visible')

      .get('a')
      .contains('Log In')
      .should('not.be.visible');
  });
});
