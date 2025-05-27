import { useState, useEffect } from 'react'
import './App.css'
import { Box, Typography, Grid, Button, Divider, TextField, Stack } from '@mui/material'
import type { Book, NewBook } from './Types'
import BookComponent from './Book'

function App() {

  const [books, setBooks] = useState<Book[]>([])
  const [bookToAdd, setBookToAdd] = useState<NewBook>({
    title: '',
    author: ''
  })

  const [addingBook, setAddingBook] = useState<boolean>(false)

  const fetchBooks = async () => {
    const response = await fetch('http://localhost:8000/books', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    const data = await response.json()
    setBooks(data)
  }

  useEffect(() => {
    fetchBooks()
  }, [])

  const handleNewBookChange = (field: keyof NewBook, value: string) => {
    setBookToAdd((prev) => ({
      ...prev,
      [field]: value,
    }))
    // console.log(bookToAdd)
  }

  const handleBookAddCancel = () => {
    setAddingBook(false)
    setBookToAdd({
      title: '',
      author: '',
    })
  }

  const handleNewBookSubmit = async () => {
    console.log(bookToAdd)
    await fetch('http://localhost:8000/books', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(bookToAdd),
    })
      .then((response) => {
        console.log('Book added successfully:', response.text())
        setAddingBook(false)
        fetchBooks()
        setBookToAdd({
          title: '',
          author: '',
        })
      }).catch((error) => {
        console.error('Error adding book:', error)
      })
  }

  return (
    <Box>
      <Typography variant="h4" align="center">
        Welcome to your Reading List!
      </Typography>
      <Typography variant="h5" align="center">
        This is a simple app to keep track of your reading list.
      </Typography>
      <Box>
        {books.length > 0 ? (
          <Grid container spacing={2} justifyContent="center">
            {books.map((book) => (
              <BookComponent key={book.id} book={book} />
            ))}
          </Grid>
        ) : (
          <Typography variant="h6" align="center">
            No books found. Please add some books to your reading list.
          </Typography>
        )}
        <Button variant="contained" color="primary" onClick={() => setAddingBook(true)}>
          Add Book
        </Button>
        {addingBook && (
          <>
            <Divider sx={{ backgroundColor: 'white' }} />
            <Box component='form' noValidate autoComplete='off'>
              <TextField
                sx={{ color: 'white' }}
                label="Title"
                variant="outlined"
                fullWidth
                margin="normal"
                onChange={(e) => handleNewBookChange('title', e.target.value)}
                value={bookToAdd.title}
              />
              <TextField
                label="Author"
                variant="outlined"
                fullWidth
                margin="normal"
                onChange={(e) => handleNewBookChange('author', e.target.value)}
                value={bookToAdd.author}
              />
            </Box>
            <Stack spacing={2} direction="row" justifyContent="center">
              <Button variant="contained" color="secondary" onClick={() => handleBookAddCancel()}>
                Cancel
              </Button>
              <Button variant="contained" color="primary" onClick={handleNewBookSubmit}>
                Submit New Book
              </Button>
            </Stack>
          </>
        )}
      </Box>
    </Box>
  )
}

export default App
