describe('Dashboard', () => {
  it('Checks if everything is in the page and work correctly', () => {
    cy.visit('http://0.0.0.0:8501')

    // Check that the title and the input exist
    cy.get('[id="prediction-de-prix-de-maison"]').should('exist')
    cy.get('[data-baseweb="input"]').should('exist')

    // Check that clicking on the button increment the value in the input
    // Check the value
    cy.get('[data-baseweb="input"]')
      .invoke('text')
      .then(Number)
      .then((n) => {
    cy.get('[data-baseweb="input"]').get('button').click({ multiple: true })
    // Check the incremented value
    cy.contains('[data-baseweb="input"]', String(n + 1))
  })

  })
})
