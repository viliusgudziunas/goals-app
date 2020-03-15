import faker from 'faker';

const email = faker.internet.email();
const password = faker.internet.password();

describe('Register', () => {
  it('should display the registration form', () => {
    cy.visit('/register')
      .get('h1')
      .contains('Register')

      .get('form');
  });

  it('should allow a user to register', () => {
    // register user
    cy.visit('/register')
      .get('input[name="email"]')
      .type(email)

      .get('input[name="password"]')
      .type(password)

      .get('button[type="submit"]')
      .click();

    // assert user is redirected to "/"
    // assert "/" is displayed properly
    cy.contains('All Users');

    cy.get('h1').contains('All Users');

    cy.contains(email);

    cy.get('.navbar-collapse').within(() => {
      cy.get('a')
        .contains('User Status')

        .get('a')
        .contains('Log Out')

        .get('a')
        .contains('Log In')
        .should('not.be.visible')

        .get('a')
        .contains('Register')
        .should('not.be.visible');
    });
  });
});
